param(
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$profilePath = Join-Path $root ".github/repository-about.json"

if (-not (Test-Path -LiteralPath $profilePath)) {
    throw "Missing GitHub About profile: $profilePath"
}

$profile = Get-Content -LiteralPath $profilePath -Raw -Encoding UTF8 | ConvertFrom-Json

Write-Host "Repository: $($profile.repository)"
Write-Host "Description: $($profile.description)"
Write-Host "Topics: $($profile.topics -join ', ')"

if ($DryRun) {
    Write-Host "Dry run: GitHub repository settings were NOT changed."
    exit 0
}

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    throw "GitHub CLI not found. Install it, then run 'gh auth login' on your computer."
}

gh auth status *> $null
if ($LASTEXITCODE -ne 0) {
    throw "GitHub CLI is not authenticated. Run 'gh auth login' locally first."
}

$topicCsv = $profile.topics -join ','
gh repo edit $profile.repository --description $profile.description --add-topic $topicCsv
if ($LASTEXITCODE -ne 0) {
    throw "Could not apply GitHub About metadata. Check account repository admin permission."
}

$description = gh api "repos/$($profile.repository)" --jq '.description'
if ($LASTEXITCODE -ne 0 -or $description -ne $profile.description) {
    throw "Description verification failed; inspect the repository About section."
}

$topicList = gh api "repos/$($profile.repository)/topics" --jq '.names | join(",")'
if ($LASTEXITCODE -ne 0) {
    throw "Topics verification request failed."
}
$actualTopics = @($topicList -split ',')
$missingTopics = @($profile.topics | Where-Object { $_ -notin $actualTopics })
if ($missingTopics.Count -gt 0) {
    throw "Some topics are missing after update: $($missingTopics -join ', ')"
}

Write-Host "Verified GitHub About description and topics successfully."
