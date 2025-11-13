function areYouPlayingBanjo(name) {
  // Implement me
  if(name.includes("r" || "R")){
    return (name + " plays banjo")
  }
  else return (name + " does not plays banjo")
}
console.log(areYouPlayingBanjo("Rakeesh"))