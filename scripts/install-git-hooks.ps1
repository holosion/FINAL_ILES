# Installs a local git hook that removes Cursor co-author trailers from commits.
$ErrorActionPreference = "Stop"

$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$hookSource = Join-Path $root "scripts/prepare-commit-msg"
$hookTarget = Join-Path $root ".git/hooks/prepare-commit-msg"

Copy-Item -Path $hookSource -Destination $hookTarget -Force
Write-Host "Installed prepare-commit-msg hook at $hookTarget"
