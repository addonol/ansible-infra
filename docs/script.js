window.showSection = function(sectionId) {
    document.querySelectorAll('.content-section').forEach(s => {
        s.classList.remove('active');
    });

    const target = document.getElementById(sectionId);
    if (target) {
        target.classList.add('active');
    }

    const links = document.querySelectorAll('.nav-link');
    links.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('onclick') && link.getAttribute('onclick').includes(sectionId)) {
            link.classList.add('active');
        }
    });

    window.scrollTo({ top: 0, behavior: 'smooth' });
};

function openZoom() {
    const overlay = document.getElementById("zoomOverlay");
    if (overlay) overlay.style.display = "flex";
}

function closeZoom() {
    const overlay = document.getElementById("zoomOverlay");
    if (overlay) overlay.style.display = "none";
}

async function initSite() {
    try {
        const respNav = await fetch('sections/side-nav.html');
        document.getElementById('nav-placeholder').innerHTML = await respNav.text();

        const main = document.getElementById('main-content');

        const sections = [
            'home.html',
            'airflow/airflow-arch.html',
            'airflow/airflow-components.html',
            'airflow/airflow-config.html',
            'airflow/airflow-auth.html',
            'infrastructure/infra-security.html',
            'infrastructure/infra-roles.html',
            'infrastructure/infra-deployment.html',
            'infrastructure/infra-rabbitmq.html',
            'footer.html'
        ];

        for (const file of sections) {
            const resp = await fetch(`sections/${file}`);
            const html = await resp.text();
            main.insertAdjacentHTML('beforeend', html);
        }

        window.showSection('home');

    } catch (err) {
        console.error("Erreur d'initialisation :", err);
    }
}

window.toggleMenu = function(menuId, btn) {
    const menu = document.getElementById(menuId);
    if (menu) {
        const isOpen = menu.classList.toggle('open');
        btn.classList.toggle('active');
        if (isOpen) {
            menu.style.maxHeight = menu.scrollHeight + "px";
        } else {
            menu.style.maxHeight = "0px";
        }
    }
};

window.openZoom = function() {
    const clickedImg = event.target; // On récupère l'image sur laquelle on a cliqué
    const overlay = document.getElementById("zoomOverlay");
    const zoomedImg = document.getElementById("zoomedImg");

    if (overlay && zoomedImg) {
        zoomedImg.src = clickedImg.src; // On copie la source de l'image cliquée vers le zoom
        overlay.style.display = "flex";
    }
};

window.closeZoom = function() {
    const overlay = document.getElementById("zoomOverlay");
    if (overlay) overlay.style.display = "none";
};

initSite();
