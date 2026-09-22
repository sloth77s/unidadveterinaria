// Tailwind CSS Configuration - UCIVET
// Shared across all pages

window.tailwindConfig = {
  theme: {
    extend: {
      colors: {
        brand: {
          royalBlue: '#0D3880',
          deepNavy: '#071F48',
          brightBlue: '#1248A4',
          navy: '#071F48',
          gold: '#E5B842',
          goldDark: '#C79A2B',
          goldLight: '#F3D275',
          slateBg: '#071F48',
          darkSlate: '#0F172A',
          mutedSlate: '#94A3B8',
          whatsapp: '#25D366'
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif']
      }
    }
  }
};

// Apply config when Tailwind loads
if (typeof tailwind !== 'undefined') {
  tailwind.config = window.tailwindConfig;
} else {
  document.addEventListener('DOMContentLoaded', function() {
    if (typeof tailwind !== 'undefined') {
      tailwind.config = window.tailwindConfig;
    }
  });
}