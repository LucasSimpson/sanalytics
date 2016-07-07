
$(function() {
    console.log('hello from index!');
    
    var A = sanalytics;

    data = {
        'page_name': 'index',
    }
    A.registerEvent('localhost', 'PAGE_LOAD', data);
});