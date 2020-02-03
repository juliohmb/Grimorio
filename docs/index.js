document.querySelector("input#text").addEventListener("keyup", function(){
    var checks = []
    checks = document.querySelectorAll("input.checkBox")
    for (var i = 0;i < checks.length; i++){
        if(checks[i].checked == true){
            listarMagias(document.querySelector("input#text").value, checks[i].id)
        }
    }
})


function listarMagias(input, checked){
    document.body.querySelector("div.magias").innerHTML = ""
    // console.log(input)
    // console.log(checked)
    if(input == ""){
        var copyed = magias
        printMagias(copyed)
    }
    else if(checked == "nome"){
        var copyed = {}
        for (var i in magias){
            if(i.includes(input.toUpperCase())){
                copyed[i] = magias[i]
            }
        }
        printMagias(copyed)
    }
    else if(checked == "nivel"){
        var copyed = {}
        for (var i in magias){
            if(magias[i]["nivel"].toUpperCase().includes(input.toUpperCase())){
                copyed[i] = magias[i]
            }
        }
        printMagias(copyed)
    }
    else if(checked == "tempo"){
        var copyed = {}
        for (var i in magias){
            if(magias[i]["tempo de conjuracao"].toUpperCase().includes(input.toUpperCase())){
                copyed[i] = magias[i]
            }
        }
        printMagias(copyed)
    }
    else if(checked == "alcance"){
        var copyed = {}
        for (var i in magias){
            if(magias[i]["alcance"].toUpperCase().includes(input.toUpperCase())){
                copyed[i] = magias[i]
            }
        }
        printMagias(copyed)
    }
    else if(checked == "componentes"){
        var copyed = {}
        for (var i in magias){
            if(magias[i]["componentes"].toUpperCase().includes(input.toUpperCase())){
                copyed[i] = magias[i]
            }
        }
        printMagias(copyed)
    }
    else if(checked == "duracao"){
        var copyed = {}
        for (var i in magias){
            if(magias[i]["duracao"].toUpperCase().includes(input.toUpperCase())){
                copyed[i] = magias[i]
            }
        }
        printMagias(copyed)
    }
    else if(checked == "descricao"){
        var copyed = {}
        for (var i in magias){
            if(magias[i]["descricao"].toUpperCase().includes(input.toUpperCase())){
                copyed[i] = magias[i]
            }
        }
        printMagias(copyed)
    }
}


function printMagias(copy){
    for(var i in copy){
        var divMagia = document.createElement("div")
        var divBorder = document.createElement("div")
        var divHead = document.createElement("div")
        var divBody = document.createElement("div")
        var divTempo = document.createElement("div")
        var divAlcance = document.createElement("div")
        var divComponentes = document.createElement("div")
        var divDuracao = document.createElement("div")
        var divDescricao = document.createElement("div")
        divMagia.className = "magia"
        divBorder.className = "border"
        divHead.className = "head"
        divBody.className = "body"
        divTempo.className = "tempoDeConjuracao"
        divAlcance.className = "alcance"
        divComponentes.className = "componentes"
        divDuracao.className = "duracao"
        divDescricao.className = "descricao"
        var h3Tempo = document.createElement("h3")
        var h3Alcance = document.createElement("h3")
        var h3Componentes =  document.createElement("h3")
        var h3Duracao = document.createElement("h3")
        var h3Descricao = document.createElement("h3")
        var h1Nome = document.createElement("h1")
        h3Tempo.innerHTML = "Tempo de conjuração:"
        h3Alcance.innerHTML = "Alcance:"
        h3Componentes.innerHTML = "Componentes:"
        h3Duracao.innerHTML = "Duração:"
        h3Descricao.innerHTML = "Descrição:"
        h1Nome.className = "nome"
        h1Nome.innerHTML = i

        var pTempo = document.createElement("p")
        var pAlcance = document.createElement("p")
        var pComponentes = document.createElement("p")
        var pDuracao = document.createElement("p")
        var pDescricao = document.createElement("p")
        var h4Nivel = document.createElement("h4")
        h4Nivel.className = "nivel"
        for (var j in copy[i]){
            if(j == "nivel"){
                h4Nivel.innerHTML = copy[i][j]
            }
            if(j == "tempo de conjuracao"){
                pTempo.innerHTML = copy[i][j]
            }
            if (j == "alcance"){
                pAlcance.innerHTML = copy[i][j]
            }
            if(j == "componentes"){
                pComponentes.innerHTML = copy[i][j]
            }
            if(j == "duracao"){
                pDuracao.innerHTML = copy[i][j]
            }
            if(j == "descricao"){
                pDescricao.innerHTML = copy[i][j]
            }
        }
        divHead.appendChild(h1Nome)
        divHead.appendChild(h4Nivel)

        divTempo.appendChild(h3Tempo)
        divTempo.appendChild(pTempo)

        divAlcance.appendChild(h3Alcance)
        divAlcance.appendChild(pAlcance)

        divComponentes.appendChild(h3Componentes)
        divComponentes.appendChild(pComponentes)

        divDuracao.appendChild(h3Duracao)
        divDuracao.appendChild(pDuracao)

        divDescricao.appendChild(h3Descricao)
        divDescricao.appendChild(pDescricao)

        divBody.appendChild(divTempo)
        divBody.appendChild(divAlcance)
        divBody.appendChild(divComponentes)
        divBody.appendChild(divDuracao)
        divBody.appendChild(divDescricao)

        divMagia.appendChild(divBorder)
        
        divBorder.appendChild(divHead)
        divBorder.appendChild(divBody)
        document.body.querySelector("div.magias").appendChild(divMagia)
    }
}

var magias
var req = new XMLHttpRequest()
req.open("GET", "./testes.json", true)
req.send()

req.onreadystatechange = function(){
    if(req.readyState == 4 && req.status == 200){
        // console.log(req.response)
        magias = JSON.parse(req.response).magias
        listarMagias("", "nome")
    }
}