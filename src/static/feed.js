document.addEventListener("DOMContentLoaded", () => {
    const raw = localStorage.getItem("crawlHistory");

    if (!raw) {
        console.log("No crawl history found");
        return;
    }

    const history = JSON.parse(raw);

    // Use the most recent crawl
    const latest = history[history.length - 1];

    renderFeed(latest.result);
});



function renderFeed(results) {
    const feed = document.getElementById("feed");
    feed.innerHTML = "";

    for (const [url, page] of Object.entries(results)) {
        const card = document.createElement("div");
        card.className = "card";

        const imageUrl = page.image_urls?.[0] || ""; // first image or empty string
        const imageStyle = imageUrl ? `background-image: url('${imageUrl}');` : "";

        card.innerHTML = `
            <div class="image" style="${imageStyle}"></div>

            <div class="content">
                <div class="title">${page.h1 || "Untitled page"}</div>

                <div class="blurb">${page.first_paragraph || "No description available."}</div>

                <div class="meta">${url}</div>

                <div class="actions">
                    <a href="${page.url}" target="_blank" rel="noopener">Read more</a>
                </div>
            </div>
        `;

        feed.appendChild(card);
    }
}