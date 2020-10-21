

f = $( function() {
    	$( "tbody" ).sortable({
    		handle: ".handle"

    	});
    	
    	$('tbody').css('border', 'solid 3px red')
  	} );



/*const saveOrderingButton = document.getElementById('saveOrdering');
const orderingForm = document.getElementById('orderingForm');
const formInput = orderingForm.querySelector('#orderingInput');

	function saveOrdering() {
	    const rows = document.getElementById("groups").querySelectorAll('tr');
	    let ids = [];
	    for (let row of rows) {
	        ids.push(row.dataset.lookup);
	    }
	    formInput.value = ids.join(',');
	    orderingForm.submit();
	    saveOrderingButton.addEventListener('click', saveOrdering);
	}*/