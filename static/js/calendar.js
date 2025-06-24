document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('appointmentForm');
  
    // Animar campos al focus y blur
    form.querySelectorAll('input, textarea').forEach(input => {
      input.addEventListener('focus', () => {
        input.style.transition = 'box-shadow 0.3s ease';
        input.style.boxShadow = '0 0 10px rgba(52, 152, 219, 0.5)';
      });
      input.addEventListener('blur', () => {
        input.style.boxShadow = 'none';
      });
    });
  
    // Validación simple para añadir animación en error
    form.addEventListener('submit', (e) => {
      let valid = true;
  
      // Campos requeridos
      ['nombre', 'email', 'fecha', 'hora', 'motivo'].forEach(id => {
        const field = document.getElementById(id);
        if (!field.value.trim()) {
          valid = false;
          field.classList.add('input-error');
          // Animación shake
          field.animate([
            { transform: 'translateX(0)' },
            { transform: 'translateX(-5px)' },
            { transform: 'translateX(5px)' },
            { transform: 'translateX(0)' }
          ], { duration: 300, iterations: 2 });
        } else {
          field.classList.remove('input-error');
        }
      });
  
      if (!valid) {
        e.preventDefault();
      }
    });
  });
  