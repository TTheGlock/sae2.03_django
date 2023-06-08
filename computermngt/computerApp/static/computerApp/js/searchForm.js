document.getElementById("searchForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Empêche le rechargement de la page lors de la soumission du formulaire

    var searchTerm = document.getElementById("searchInput").value; // Récupère le terme de recherche saisi dans l'input
    var content = document.documentElement.innerHTML; // Récupère le contenu de la page

    var regex = new RegExp(searchTerm, "gi"); // Crée une expression régulière avec le terme de recherche (ignorant la casse et recherchant toutes les occurrences)

    var matches = content.match(regex); // Effectue la recherche dans le contenu de la page

    if (matches) {
      // Si des correspondances sont trouvées
      window.find(searchTerm); // Utilise la fonction de recherche intégrée du navigateur pour mettre en évidence les occurrences
    } else {
      alert("Aucune correspondance trouvée.");
    }
  });