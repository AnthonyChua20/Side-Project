let digimon = "Alphamon";

 GetDigimons =() => {
    return new Promise((resolve, reject) =>{
        if (digimon === "Omnimon") {
            resolve("Digimon is Omnimon");
        } else {
            reject("Digimon is " + digimon);}
    }
    )};

   GetDigimons().then((message) => {
    console.log(message);
}).catch((error) => {
    console.error(error);
}); 


