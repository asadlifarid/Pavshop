// window.addEventListener('load', async function(event,page){
//     let response = await fetch(`${location.origin}/api/products/`)
//     // let response = await fetch(`${location.origin}/api/products/?page=${page}`)

//     let resData = await response.json()
//     let products = document.querySelector('#products')
//     for (product of resData){
//         products.innerHTML += `
//         <div class="col-md-4">
//                 <div class="item"> 
//                   <!-- Item img -->
//                   <div class="item-img"> 
//                     <img class="img-1" src="${product.image}" alt="" >
//                     <!-- Overlay -->
//                     <div class="overlay">
//                       <div class="position-center-center">
//                         <div class="inn"><a href="#." data-lighter><i class="icon-magnifier"></i></a> <a href="{% url 'shopping_cart_page' %}"><i class="icon-basket"></i></a></div>
//                         <!-- <div class="inn"><a href="#." data-lighter><i class="icon-magnifier"></i></a> <a href="{% url 'shopping_cart_page' %}"><i class="icon-basket"></i></a> <a href="#." ><i class="icon-heart"></i></a></div> -->

//                       </div>
//                     </div>
//                   </div>

//                   <!-- Item Name -->
//                   <div class="item-name"> <a href="/product_detail/${product.slug}">${product.title}</a>
//                     <p>${product.small_description}</p>
//                   </div>
//                   <!-- Price --> 
//                   <span class="price"><small>$</small>${product.money}</span> </div>
//               </div>
        
//         `
//     }

// })





// let currentPage = 1;
// const pageSize = 4;

// function fetchData(page) {
//   const url = `${location.origin}/api/products/?page=${page}&pageSize=${pageSize}`;

//   // url.searchParams.append('page', pageNumber);
//   // url.searchParams.append('pageSize', pageSize);
  
//   fetch(url)
//   .then(response => response.json())
//   .then(data => {
//     console.log(data);

//     currentPage = page;
//   })

//   .catch(error => {
//     console.error('Error:', error);
//   });
// }

// // Call the fetchData function to fetch initial data
// fetchData(currentPage);

// // Example: Next Page Button Event Listener
// const nextButton = document.getElementById('next-button');
// nextButton.addEventListener('click', () => {
//   const nextPage = currentPage + 1;
//   fetchData(nextPage);
// });

// // Example: Previous Page Button Event Listener
// const prevButton = document.getElementById('prev-button');
// prevButton.addEventListener('click', () => {
//   if (currentPage > 1) {
//     const prevPage = currentPage - 1;
//     fetchData(prevPage);
//   }
// });





// function goToPage(pageNumber) {
//   currentPage = pageNumber;
//   fetchItems(currentPage);
// }


// function goToNextPage() {
//   currentPage++;
//   fetchItems(currentPage);
// }


// function goToPreviousPage() {
//   if (currentPage > 1) {
//     currentPage--;
//     fetchItems(currentPage);
//   }
// }



// fetchItems(currentPage);











// function fetchItems(pageNumber, pageSize) {
//   const url = new URL(`${location.origin}/api/products/?page=${pageNumber}`);
//   url.searchParams.append('page', pageNumber);
//   url.searchParams.append('pageSize', pageSize);

//   return fetch(url)
//   .then(response => response.json())
//   .then(data => {
//     console.log(data);

//   })
//   .catch(error => {
//     console.log('Error:', error)
//   });
// }


// const pageNumber = 3;
// const pageSize = 2;
// fetchItems(pageNumber, pageSize);
