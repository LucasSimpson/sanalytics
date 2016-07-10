

function registerEvent(domain, eventType, jsonData, userToken) {
    var endpoint = '/ingest/';
    var data = {
        auth_token: 'lolzeveryonesallowed',
        category: eventType,
        user: userToken === undefined ? 'anon' : userToken,
        json_data: JSON.stringify(jsonData),
    };
    console.log(data);

    console.log('doing ajax POST');

    $.ajax({
        type: "POST",
        url: endpoint,
        data: data,
        success: function(data, textStatus, xhr) {
            console.log('success!');
            console.log(data);
        },
        error: function(xhr, textStatus, errorThrown) {
            console.log('error');
            console.log(textStatus + ':: ' + errorThrown);
        },
        dataType: 'json',
    });
}


sanalytics = {
    registerEvent: registerEvent
};