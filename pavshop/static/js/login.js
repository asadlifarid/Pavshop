let loginForm = document.querySelector('#loginForm')


loginForm.addEventListener('submit', async function(){
    // event.preventDefault()
    let postData = {
        'username' : loginForm.username.value,
        'password' : loginForm.password.value
    }
    let response = await fetch(`${location.origin}/auth/token/`, {
        method : 'POST',
        body : JSON.stringify(postData),
        headers : {
            'Content-Type' : 'application/json'

        }
    })
    let resData = await response.json()
    console.log(resData)
    if (!response.ok){
        alert(resData.detail)
    }
    else{
        localStorage.setItem('token', resData.access)
        window.location.href.replace(`${location.origin}/en/profile/`)
    }
})