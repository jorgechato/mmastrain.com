$(document).on("ready",startNav);
//$(document).on("ready",linkNotes);

function startNav(){

	// Set options
    var options = {
        offset: '#showHere',
        classes: {
            clone:   'nav--clone',
            stick:   'nav--stick',
            unstick: 'nav--unstick'
        }
    };

	var banner = new Headhesive('#nav', options);
}
/*
function linkNotes(){
	$('.notas').scrollNav();
}*/