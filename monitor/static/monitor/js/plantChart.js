let first_run = true;
let myChart = '';

function display_chart(data) {
    let list_of_dates = [];
    let list_of_temps = [];
    let list_of_light = [];
    let list_of_moisture = [];
    for (let index = 0; index < data.sensor_data.length; index++) {
        list_of_dates.push(data.sensor_data[index].datetime);
        list_of_temps.push(data.sensor_data[index].temperature);
        list_of_light.push(data.sensor_data[index].light);
        list_of_moisture.push(data.sensor_data[index].moisture);
    }

    var ctx = document.getElementById('myChart').getContext('2d');

    var lineChartData = {
        labels: list_of_dates,
        datasets: [{
            label: 'Temperature',
            backgroundColor: ['rgba(255, 99, 132, 1)'],
            borderColor: ['rgba(255, 99, 132, 1)'],
            fill: false,
            data: list_of_temps,
            yAxisID: 'y-temp',
        }, {
            label: 'Light',
            backgroundColor: ['rgba(255,204,0,1)'],
            borderColor: ['rgba(255,204,0,1)'],
            fill: false,
            data: list_of_light,
            yAxisID: 'y-light',
        }, {
            label: 'Soil moisture',
            backgroundColor: ['rgba(0,102,255,1)'],
            borderColor: ['rgba(0,102,255,1)'],
            fill: false,
            data: list_of_moisture,
            yAxisID: 'y-moisture',
        }]
    }

    myChart = new Chart(ctx, {
        type: 'line',
        data: lineChartData,
        options: {
            scales: {
                yAxes: [{
                    type: 'linear',
                    display: true,
                    position: 'left',
                    id: 'y-temp',
                    ticks: {
                        beginAtZero: true,
                    },
                    scaleLabel: {
                        display: true,
                        labelString: "Temperature °c",
                    }
                }, {
                    type: 'linear',
                    display: false,
                    position: 'right',
                    id: 'y-light',
                    ticks: {
                        beginAtZero: true,
                    },
                }, {
                    type: 'linear',
                    display: true,
                    position: 'right',
                    id: 'y-moisture',
                    ticks: {
                        beginAtZero: true,
                    },
                    scaleLabel: {
                        display: true,
                        labelString: "Light  /  Moisture"
                    }
                }]
            },
            legend: {
                position: 'bottom'
            },
            title: {
                display: true,
                // text: current_temp + "°",
                text: "Apache Chilli Plant",
                fontSize: 100,
            }
        }
    });
}

function get_stats() {
    $.ajax({
        url: '/monitor/sensordata/',
        type: 'GET',
        dataType: 'json',
        success: function(result) {
            display_chart(result);
        },
        error: function(result) {
            console.log("Failed");
        }
    })
}

$(document).ready(function() {
    get_stats();
});