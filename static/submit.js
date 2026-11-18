const form = document.querySelector("#form");
const purge = document.querySelector("#purge")
const statusText = document.querySelector("#status");
const player = document.querySelector("#player");
const downloadLink = document.querySelector("#downloadLink");

async function sendData(){
    const formData = new FormData(form);

    statusText.textContent="Downloading . . .";
    const submitBtn = form.querySelector('input[type="submit"]')
    player.removeAttribute("src");
    downloadLink.hidden = true;
    submitBtn.disabled = true;
    try{
        const response = await fetch("/download", {
            method: "POST",
            body: formData,
        });
        const data = await response.json();
        console.log(data);
        
        if(data.ok){
            statusText.textContent = "Done: " + data.title;
            player.src = data.url;
            downloadLink.href=data.download_url;
            downloadLink.hidden=false;
        }else{
            statusText.textContent = "Error: " + data.error;
        }

    } catch(e){
        console.error(e);
        statusText.textContent = "Error: could not reach server"
    }finally{
        submitBtn.disabled = false;
    }
}

async function purgeData(){
    purge.disabled = true;
    // release the file the player is holding (Windows won't delete open files)
    player.pause();
    player.removeAttribute("src");
    player.load();
    downloadLink.hidden = true;

    try{
        const response = await fetch("/files", { method: "DELETE" });
        const data = await response.json();
        statusText.textContent = data.ok
            ? `Deleted ${data.deleted} file(s)`
            : "Some files couldn't be deleted: " + data.failed.join(", ");
    }catch(e){
        console.error(e);
        statusText.textContent = "Error: could not reach server";
    }finally{
        purge.disabled = false;
    }
}

purge.addEventListener("click", (event) => {
    event.preventDefault();
    purgeData();
});


form.addEventListener("submit", (event) => {
    event.preventDefault();
    sendData();
})


