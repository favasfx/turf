document.addEventListener("DOMContentLoaded", function(event) {
   
    const showNavbar = (toggleId, navId, bodyId, headerId) => {
        const toggle = document.getElementById(toggleId),
        nav = document.getElementById(navId),
        bodypd = document.getElementById(bodyId),
        headerpd = document.getElementById(headerId)
        
        // Validate that all variables exist
        if(toggle && nav && bodypd && headerpd){
        toggle.addEventListener('click', ()=>{
        // show navbar
        nav.classList.toggle('show')
        // change icon
        toggle.classList.toggle('bx-x')
        // add padding to body
        bodypd.classList.toggle('body-pd')
        // add padding to header
        headerpd.classList.toggle('body-pd')
        })
        }
    }
    
    showNavbar('header-toggle','nav-bar','body-pd','header')
    
    /*===== LINK ACTIVE =====*/
    const linkColor = document.querySelectorAll('.nav_link')
    
    function colorLink(){
    if(linkColor){
    linkColor.forEach(l=> l.classList.remove('active'))
    this.classList.add('active')
    }
    }
    linkColor.forEach(l=> l.addEventListener('click', colorLink))
    
     // Your code to run since DOM is loaded and ready
    });


function editBookings(id){
    console.log(id)

    $.ajax({
        url:"edit_Bookings",
        type:"post",
        data: {
            'id': id,
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response) {
            console.log(response.data)
            // document.getElementById('delete_url').href='delete_employee_data/'+response.data.id
            console.log(response.data)
            $('#id').val(response.data.id)
            $('#uid').val(response.data.id)
            $('#name').val(response.data.name)
            $('#phone').val(response.data.phone)
            $('#email').val(response.data.email)
            $('#date').val(response.data.date)
            $('#time').val(response.data.time)
            $('#status').val(response.data.status)
     
        }
    })
}