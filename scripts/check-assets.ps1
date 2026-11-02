$ErrorActionPreference = 'Stop'
Set-Location (Split-Path -Parent $PSScriptRoot)

$server = Join-Path (Get-Location) 'runtime\llama-server.exe'
$model = Join-Path (Get-Location) 'models\qwen2.5-1.5b-instruct-q4_k_m.gguf'

Write-Host 'PREPA AI - comprobación de componentes locales'
$missing = $false
foreach ($item in @(@{Name='llama-server.exe';Path=$server},@{Name='Modelo GGUF';Path=$model})) {
    if (Test-Path -LiteralPath $item.Path -PathType Leaf) {
        $file = Get-Item -LiteralPath $item.Path
        Write-Host "[OK] $($item.Name): $($file.Length) bytes"
        Get-FileHash -LiteralPath $item.Path -Algorithm SHA256 | Format-Table -HideTableHeaders
    } else {
        Write-Host "[FALTA] $($item.Name): $($item.Path)"
        $missing = $true
    }
}
if ($missing) {
    Write-Host 'Coloca los componentes faltantes según docs/ASSETS.md.'
    exit 1
}
Write-Host 'Componentes encontrados. Falta validar la compatibilidad ejecutándolos en este equipo.'
