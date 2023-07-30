window.addEventListener('load', async function(event){
    let response_categories = await fetch(`${location.origin}/api/categories/`)
    let resData = await response_categories.json()
    console.log(resData);
    let category_select = document.querySelector('[name = "category"]')
    for (category of resData.results){
        category_select.innerHTML += `
        <option value="${category.id}">${category.name}</option>
        
        `
    }
    
    let response_tags = await fetch(`${location.origin}/api/tags/`)
    let resDataTags = await response_tags.json()
   
    console.log( resDataTags   );
    let tags_select = document.querySelector('[name = "tag"]')
    for (tag of resDataTags.results){
        tags_select.innerHTML += `
        <option value="${tag.id}">${tag.name}</option>
        `
    }
})


let storyCreationForm = document.querySelector('#storyCreationForm')
let token = localStorage.getItem('token')

storyCreationForm.addEventListener('submit', function(event){
    event.preventDefault()
   
    let formData = new FormData(storyCreationForm)
    fetch(`${location.origin}/api/stories/`, {
        method : 'POST',
        headers : {
            'Authorization' : `Bearer ${token}`
        },
        body : formData
    })
    
    .then((res)=>{
        if (res.status == "201"){ 
            console.log(res);

        } 
        else{
           
         window.location.href = `${location.origin}/en/login/`

        }
        console.log(res);

    })
    .catch((err)=>{
        console.log(err);
    })


})




// storyCreationForm.addEventListener('click', function(){
//     // event.preventDefault()
   
//     // let formData = new FormData(storyCreationForm)
//     fetch(`${location.origin}/api/stories/${pk}/`, {
//         method : 'GET',
//         headers : {
//             'Content-Type' : 'application/json'
//             // 'Authorization' : `Bearer ${token}`
//         }
//         // body : formData
//     })
    
//     // .then((res)=>{
//     //     if (res.status == "201"){ 
//     //         console.log(res);

//     //     } 
//     //     else{
           
//     //      window.location.href = `${location.origin}/en/login/`

//     //     }
//     //     console.log(res);

//     // })
//     .catch((err)=>{
//         console.log(err);
//     })


// })






// storyCreationForm.addEventListener('load', function(pk){
//     // event.preventDefault()
   
//     let formData = new FormData(storyCreationForm)
//     fetch(`${location.origin}/api/stories/${pk}/`, {
//         method : 'PUT',
//         headers : {
        
//             'Authorization' : `Bearer ${token}`
//         },
//         body : formData
//     })
    
//     .then((res)=>{
//         if (res.status == "201"){ 
//             console.log(res);

//         } 
//         else{
           
//          window.location.href = `${location.origin}/en/login/`

//         }
//         console.log(res);

//     })
//     .catch((err)=>{
//         console.log(err);
//     })


// })