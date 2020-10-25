

$( function() {
    	$( ".groups" ).sortable({
    		handle: ".handle",
            
    	});
    	
    	$('.groups').css('border', 'solid 3px red')
} );

const saveOrderingButton = document.querySelector(".saveOrdering");
const orderingForm = document.querySelector(".orderingForm");
const formInput = orderingForm.querySelector(".orderingInput");

function saveOrdering() {
    const rows = document.getElementById("groups").querySelectorAll('tr');
    let ids = [];
    for (let row of rows) {
        ids.push(row.dataset.id);
    }
    formInput.value = ids.join(',');
    orderingForm.submit();
    
    console.log(ids)
    console.log(typeof ids)
    console.log(typeof(ids[0]))
}

saveOrderingButton.addEventListener('click', saveOrdering);

/*for (var i = 0; i < saveOrderingButton.length; i++) {
   saveOrderingButton[i].addEventListener('click', saveOrdering);
   };
*/



