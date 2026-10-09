$content = Get-Content 'index.html' -Raw

$old = @"
          <a href="/contacto-y-ubicacion" class="w-full sm:w-auto px-6 py-3.5 border border-brand-gold/50 text-brand-gold hover:bg-brand-gold hover:text-white font-semibold text-base rounded-xl transition-all">
            Ubicación de la Clínica
          </a>

        </div>
"@

$new = @"
          <a href="/contacto-y-ubicacion" class="w-full sm:w-auto px-6 py-3.5 border border-brand-gold/50 text-brand-gold hover:bg-brand-gold hover:text-white font-semibold text-base rounded-xl transition-all">
            Ubicación de la Clínica
          </a>

          <a href="#especialidades" class="w-full sm:w-auto px-6 py-3.5 border border-brand-gold/50 text-brand-gold hover:bg-brand-gold hover:text-white font-semibold text-base rounded-xl transition-all">
            Ver Especialidades
          </a>

        </div>
"@

$content = $content -replace [regex]::Escape($old), $new
Set-Content 'index.html' $content -Encoding UTF8
Write-Host 'Done'