$files = Get-ChildItem "servicios\*.html"

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw
    
    # Add OG image dimensions and Twitter cards after og:image
    $content = $content -replace 
        '(<meta property="og:image" content="https://unidadveterinaria\.pages\.dev/img/og-unidad-veterinaria\.png">)',
        '$1`r`n  <meta property="og:image:width" content="1200">`r`n  <meta property="og:image:height" content="630">`r`n  <meta name="twitter:card" content="summary_large_image">`r`n  <meta name="twitter:image" content="https://unidadveterinaria.pages.dev/img/og-unidad-veterinaria.png">'
    
    # Add width/height to header logo (w-16 h-16)
    $content = $content -replace 
        '(<img src="\.\./img/logo-unidad-veterinaria\.png" alt="Logo David Aguilar" class="w-16 h-16 drop-shadow-md object-contain" loading="lazy">)',
        '$1 width="225" height="225"'
    
    # Add width/height to footer logo (w-10 h-10)
    $content = $content -replace 
        '(<img src="\.\./img/logo-unidad-veterinaria\.png" alt="Logo David Aguilar" class="w-10 h-10 object-contain" loading="lazy">)',
        '$1 width="225" height="225"'
    
    Set-Content $file.FullName $content -Encoding UTF8
    Write-Host "Fixed: $($file.Name)"
}