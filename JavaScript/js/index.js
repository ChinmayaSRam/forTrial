var cars = [
    {carName : "Innova", onRoadPrice :"2000000", yearOfModel: "2020" },
    {carName : "Dzire", onRoadPrice :"800000", yearOfModel: "2010" },
    {carName : "i20", onRoadPrice :"700000", yearOfModel: "2022" },
    {carName : "i10", onRoadPrice :"600000", yearOfModel: "2012" }
]

function displayCarDetails(){
    let carname = document.getElementById("selectCar").value
    cars.forEach(function(data){
        if(data.carName == carname)
        {
            document.getElementById("name").innerHTML = "carName: "+data.carName
            document.getElementById("price").innerHTML = "onRoadPrice: "+data.onRoadPrice
            document.getElementById("year").innerHTML = "yearOfModel: "+data.yearOfModel
        }
    })
}