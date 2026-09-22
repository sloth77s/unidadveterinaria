from pathlib import Path

path = Path(r"unidad-veterinaria-david-aguilar/index.html")
text = path.read_text(encoding="utf-8")

# Fix duplicate closing section
text = text.replace("    </section>    </section>", "    </section>", 1)

start = text.find("    <!-- RESEÑAS GOOGLE -->")
end = text.find("    <!-- SPECIALTIES GRID -->")
if start == -1 or end == -1:
    raise SystemExit(f"markers not found start={start} end={end}")

reviews = text[start:end]
rest_before = text[:start]
rest_after = text[end:]

eeat = """
    <!-- EQUIPO MÉDICO / EEAT -->
    <section class="py-14 bg-brand-deepNavy border-b border-brand-gold/20">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-8">
          <p class="text-[11px] font-bold text-brand-gold uppercase tracking-wider mb-2">Experiencia y confianza</p>
          <h2 class="text-2xl sm:text-3xl font-bold text-white">Equipo Médico y Trayectoria Profesional</h2>
        </div>
        <div class="rounded-2xl border border-brand-gold/40 bg-brand-royalBlue/10 p-6 sm:p-8 space-y-4">
          <p class="text-sm sm:text-base text-slate-200 leading-relaxed">
            La Unidad Veterinaria David Aguilar es un centro de especialidades médicas veterinarias en Villavicencio, Meta, liderado por el <strong class="text-white">Dr. David Aguilar</strong>. La atención se enfoca en medicina de alta complejidad, cuidados intensivos y consulta externa por especialidad, siempre con cita previa.
          </p>
          <p class="text-sm sm:text-base text-slate-200 leading-relaxed">
            El enfoque clínico combina diagnóstico preciso, seguimiento personalizado y criterio médico especializado para ofrecer a cada paciente un plan de manejo claro, ético y basado en evidencia.
          </p>
          <ul class="grid sm:grid-cols-2 gap-3 text-xs sm:text-sm text-slate-300 pt-2">
            <li class="flex gap-2"><span class="text-brand-gold font-bold">✓</span> Especialidades clínicas y diagnóstico avanzado</li>
            <li class="flex gap-2"><span class="text-brand-gold font-bold">✓</span> Atención exclusivamente con cita previa</li>
            <li class="flex gap-2"><span class="text-brand-gold font-bold">✓</span> Medicina de alta complejidad en Villavicencio</li>
            <li class="flex gap-2"><span class="text-brand-gold font-bold">✓</span> Comunicación clara con el tutor de la mascota</li>
          </ul>
        </div>
      </div>
    </section>

"""

marker = "    </section>\n  </main>"
close_pos = rest_after.find(marker)
if close_pos == -1:
    raise SystemExit("specialties close / main not found")

specialties_block = rest_after[: close_pos + len("    </section>\n")]
tail = rest_after[close_pos + len(marker) :]
new_after = specialties_block + eeat + reviews + "  </main>" + tail

final = rest_before + new_after
path.write_text(final, encoding="utf-8")

print("OK")
print("duplicate_fixed", "    </section>    </section>" not in final)
print("h4_count", final.count("<h4"))
print("eeat", "Equipo Médico y Trayectoria Profesional" in final)
print("order_ok", final.find("Especialidades Médicas Clínicas") < final.find("Equipo Médico y Trayectoria Profesional") < final.find("Lo que dicen nuestros clientes"))
