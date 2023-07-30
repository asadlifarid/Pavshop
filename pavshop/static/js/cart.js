// console.log('hello world')
var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)

        console.log('USER', user)
        if(user === 'AnonymousUser'){
            console.log('Not logged in')
        }else{
            updateUserOrder(productId, action)
        }
    })
}



function updateUserOrder(productId, action){
    console.log('User is logged in, sending data..')

    // var url = 'http://127.0.0.1:8000/en/update_item/'
    var url = `${location.origin}/en/update_item/`


    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json'
            // 'Authorization': `Bearer ${localStorage.getItem('token')}`
            // 'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action':action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:', data)
        location.reload()
    });

}

























// function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         const cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             const cookie = cookies[i].trim();
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
// const csrftoken = getCookie('csrftoken');





// let btns = document.querySelectorAll(".shop-detail button")


// btns.forEach(btn=>{
//     btn.addEventListener("click", addToCart)
// })

// function addToCart(e){
//     let productsid = e.target.value
//     let url = "/add_to_cart/"
    
//     let data = {id:productsid}

//     fetch('http://127.0.0.1:8000/api/orders/', {
//         method: "POST",
//         headers: {"Content-Type":"application/json", 'X-CSRFToken': csrftoken},
//         body: JSON.stringify(data)
//     })
//     .then(res=>res.json())
//     .then(data=>{
//         console.log(data)
//     })
//     .catch(error=>{
//         console.log(error)
//     })

    
// }









// var updateBttns = document.getElementsByClassName('update-cart')


// for(var i = 0; i < updateBttns.length; i++){
//     updateBttns[i].addEventListener('click', function(event){
//         event.preventDefault()

//         var productId = this.dataset.product
//         var action = this.dataset.action
//         console.log('productId:', productId, 'Action:', action)

//         console.log('USER:', user)
//         if(user === 'AnonymousUser')
//         {
//             console.log('Not logged in')
//         }
//         else
//         {
//             // updateUserOrder(productId, action)
//             console.log('User is logged in, sending data...')
//         }
//     })
// }



// function updateUserOrder(productsId, action){
//     console.log('User is logged in, sending data..')

//     var url = '/update_item/'

//     fetch('http://127.0.0.1:8000/api/orders/', {
//         method: 'POST',
//         headers: {
//             'Content-Type':'application/json',
//             'X-CSRFToken':csrftoken,
//         },
//         body: JSON.stringify({'productsId': productsId, 'action':action})
//     })

//     .then((response) =>{
//         return response.json()
//     })

//     .then((data) =>{
//         console.log('data:', data)
//         location.reload()
//     })
// }




// const BasketLogic = {
//     url: `${location.origin}/api/basket/`,

//     addProduct(productId, quantity) {
//         return fetch(`${this.url}`, {
//             method: 'POST',
//             credentials: 'include',
//             headers: {
//                 'Content-type': 'application/json',
//                 'Authorization': `Bearer ${localStorage.getItem('token')}`,
//                 'X-CSRFToken': csrftoken
//             },
//             body: JSON.stringify({
//                 'product_id': productId,
//                 'quantity': quantity,
//             })
//         }).then(response => response.json()).then(data => {
//             console.log(data);
//             if (data.success) {
//                 window.alert(data.message);
//             }
//             document.getElementById('cart-sidebar').innerHTML = "";
//             for (let i in data) {
//                 document.getElementById('cart-sidebar').innerHTML += `<ul class="row cart-details">
//             <li class="col-sm-6">
//               <div class="media"> 
//                 <!-- Media Image -->
//                 <div class="media-left media-middle"> <a href="#." class="item-img"> <img class="media-object" src="${i.image}" alt=""> </a> </div>
                
//                 <!-- Item Name -->
//                 <div class="media-body">
//                   <div class="position-center-center">
//                     <h5>wood chair${i.title}</h5>
//                     <p>Lorem ipsum dolor sit amet</p>
//                   </div>
//                 </div>
//               </div>
//             </li>
            
//             <!-- PRICE -->
//             <li class="col-sm-2">
//               <div class="position-center-center"> <span class="price"><small>$</small>${i.money}</span> </div>
//             </li>
            
//             <!-- QTY -->
//             <li class="col-sm-1">
//               <div class="position-center-center">
//                 <div class="quinty"> 
//                   <!-- QTY -->
//                   <select class="selectpicker">
//                     <option>1</option>
//                     <option>2</option>
//                     <option>3</option>
//                   </select>
//                 </div>
//               </div>
//             </li>
            
//             <!-- TOTAL PRICE -->
//             <li class="col-sm-2">
//               <div class="position-center-center"> <span class="price"><small>$</small>299</span> </div>
//             </li>
            
//             <!-- REMOVE -->
//             <li class="col-sm-1">
//               <div class="position-center-center"> <a href="#." class="button remove-item" data="${item.id}" title="Remove item"><i class="icon-close"></i></a> </div>
//             </li>
//           </ul>`;
//             }
//         });
//     },
// }

// const addToBasket = document.getElementById('add-to-basket');
// addToBasket.onclick = function () {
//     const productId = this.getAttribute('data');
//     const quantity = parseInt(document.getElementById('qty').value)
//     BasketLogic.addProduct(productId, quantity);

// }



// let addToCard = document.getElementsByClassName('btn-cart');
// for (let i = 0; i < addToCard.length; i++) {
//     addToCard[i].onclick = function () {
//         const productId = this.getAttribute('data');
//         const quantity = 1;
//         BasketLogic.addProduct(productId, quantity);

//     }
// }