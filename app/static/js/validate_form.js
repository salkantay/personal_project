function validate_search(){
    var est_name = document.getElementById('est-name');
    var est_address = document.getElementById('est-address');
    var business_type = document.getElementById('business-type');
    var counter = 0;

    var arr = [est_name, est_address, business_type]

    for(i in arr){
        if(!arr[i].value || (arr[i] === "")){
            counter++;
        }
    }

    if(counter > 0){
        document.getElementById('search-ratings').disabled = false;
    } else {
        document.getElementById('search-ratings').disabled = true;
    }
}