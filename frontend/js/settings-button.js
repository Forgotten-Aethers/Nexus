window.addEventListener("load", () => {
    console.log("App cargada")
    
    const settingsbutton = document.querySelector(".settings-button");

    settingsbutton.addEventListener("click", () => {
        console.log("Settings-button: Clicked")
    });
});