// @ts-nocheck

$("#tab-left a").on("click", function (e) {
	e.preventDefault();
	$(this).tab("show");
});

$("#tab-right a").on("click", function (e) {
	e.preventDefault();
	$(this).tab("show");
});

/* tab navigation persistence*/

$("#tab-left a").on("shown.bs.tab", function (e) {
	var hash = $(e.target).attr("href");
	if (history.pushState) {
		history.pushState(null, null, hash);
	} else {
		location.hash = hash;
	}
});

$("#tab-right a").on("shown.bs.tab", function (e) {
	var hash = $(e.target).attr("href");
	if (history.pushState) {
		history.pushState(null, null, hash);
	} else {
		location.hash = hash;
	}
});

var hash = window.location.hash;
if (hash) {
	$('.nav-link[href="' + hash + '"]').tab("show");
}
