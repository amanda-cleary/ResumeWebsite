document.addEventListener('DOMContentLoaded', () => {
    const headerMount = document.getElementById('site-header');

    if (!headerMount) {
        return;
    }

    const isRecipePage = window.location.pathname.includes('/recipes/');
    const prefix = isRecipePage ? '../' : '';
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';

    headerMount.innerHTML = `
    <header>
      <h1>Amanda Cleary</h1>
      <nav>
        <a href="${prefix}index.html" class="nav-btn ${currentPage === 'index.html' ? 'is-active' : ''}">About</a>
        <a href="${prefix}experiences.html" class="nav-btn ${currentPage === 'experiences.html' ? 'is-active' : ''}">Experiences</a>
        <a href="${prefix}portfolio.html" class="nav-btn ${currentPage === 'portfolio.html' ? 'is-active' : ''}">Portfolio</a>
      </nav>
    </header>
  `;
});

document.addEventListener('DOMContentLoaded', () => {
    const footerMount = document.getElementById('site-footer');

    if (!footerMount) {
        return;
    }

    const isRecipePage = window.location.pathname.includes('/recipes/');
    const prefix = isRecipePage ? '../' : '';

    footerMount.innerHTML = `
    <footer class="site-footer">
        <p class="footer-name">&copy; ${new Date().getFullYear()} Amanda Cleary</p>
        
    </footer>
  `;
});
