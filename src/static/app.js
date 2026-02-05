console.log("APP JS LOADED");

document.addEventListener("DOMContentLoaded", () => {
    console.log("DOM READY");

    const form = document.getElementById("crawl-form");

    if (!form) {
        console.warn("crawl-form not found on this page");
        return;
    }

    let currentJobId = null;

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        document.getElementById("status").textContent = "Starting crawl...";
        document.getElementById("results").textContent = "";

        const payload = {
            base_url: document.getElementById("url").value,
            max_pages: parseInt(document.getElementById("max_pages").value),
            max_concurrency: parseInt(document.getElementById("max_concurrency").value)
        };

        const response = await fetch("/crawl", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        const data = await response.json();
        currentJobId = data.job_id;

        pollStatus();
    });

    async function pollStatus() {
        if (!currentJobId) return;

        console.log("Polling", currentJobId);

        const response = await fetch(`/crawl/${currentJobId}`);
        const data = await response.json();

        document.getElementById("status").textContent = data.status;

        if (data.status === "Completed") {
            saveCrawlResult(currentJobId, data.result);
            document.getElementById("results").textContent =
                "Crawl saved. View results on the feed page.";
            return;
        }

        if (data.status === "Failed") {
            document.getElementById("results").textContent =
                `Error: ${data.error}`;
            return;
        }

        setTimeout(pollStatus, 1000);
    }

    function saveCrawlResult(jobId, result) {
        console.log("Saving crawl", jobId);

        const raw = localStorage.getItem("crawlHistory");
        const history = raw ? JSON.parse(raw) : [];

        history.push({
            jobId,
            timestamp: Date.now(),
            result
        });

        localStorage.setItem("crawlHistory", JSON.stringify(history));
    }
});
