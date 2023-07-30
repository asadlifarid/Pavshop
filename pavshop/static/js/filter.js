// let filterCategory = document.getElementsByClassName("category");

// // filterCategory[0].innerHTML = '';
// // console.log(filterCategory)
// for (let i = 0; i < filterCategory.length; i++){
//     filterCategory[i].onclick = function() {
//         const categoryId = this.getAttribute('data');
//         FilterLogic.filterProduct(categoryName);
//     }

// }







// window.addEventListener('load', async function(){
//     // event.preventDefault()
//     let response = await fetch(`${location.origin}/api/products/categories/`)
//     // let response = await fetch(`${location.origin}/api/products/?page=${page}`)
//     console.log(response)
//     let result = await response.json()
//     console.log(result)
//     let categorys = document.querySelector('.category')
//     for (cat of result.results){
//         categorys.innerHTML += `
//         <li><a href="?category=${cat.name}"> ${cat.name} <span>${product.products.count}</span></a></li>
        
        
//         `
//     }

// })






// let response =  await fetch(`${location.origin}/api/products/categories/`)
// let resData = await response.json()
// let categories = document.querySelector('.category')
// console.log(categories)
// for (cat of resData){
//     console.log(resData)
//     categories.innerHTML += `
                 
//         <li><a href="?category={{product.name.split|join:''}}"> ${cat.name} <span>({{product.products.count}}){{ product.num_products }}</span></a></li>
//                 `
    
// }
//   .then(data => {
//     data.forEach(category => {
//         const categoryId = category.id;
//         const categoryName = category.name;


//         const categoryItem = document.getElementById('categoryId');
        
//     });
//   })

// .catch(error => {
//     console.error('Error:', error);
// });














// const FilterLogic = {
//     url: `${location.origin}/api/products/`,
//     // let response = await fetch(`${location.origin}/api/products/categories/`)


//     filterProduct(categoryName) {
//         let url = this.url;
//         if (categoryName) {
//             url += `?category=${categoryName}`;
//         }
//         fetch(url).then(res => res.json().then(data => {
//             document.querySelector('#products').innerHTML = ""
//             for (let i in data) {
//                 console.log(data)
//                 for (let x in data[i].category) {
//                     if (data[i]['category'][x] == categoryName) {
//                         console.log(data[i]['category'][x]);
//                         console.log(data[i]);
//                         document.getElementsByClassName('category').innerHTML += `
//                        <li><a href="?category=${i.name}"> ${i.name} <span>(${i.products.count})${data[i].num_products}</span></a></li>

                          
//                         `
//                     }
//                 }
//             }

//         }))
//     }
// }