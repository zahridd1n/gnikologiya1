document.addEventListener('mousemove', (e) => {
    let x = e.clientX / window.innerWidth;
    let y = e.clientY / window.innerHeight;
    
    document.documentElement.style.setProperty('--swing-x', (x - 0.5) * 200);
    document.documentElement.style.setProperty('--swing-y', (y - 0.5) * 200);
  });
  