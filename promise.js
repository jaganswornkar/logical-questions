const myPromise = new Promise((resolve, reject)=>{
    setTimeout(() => {
        resolve('Hello moto')
    }, 3000);
})

// if promise resolved 
let p2 = myPromise.then((data)=>{
    console.log('resolved data : ',data)
    return data
})

// if promise rejected
myPromise.catch((err)=>{
    console.error('rejected promise : ',err)
})

// for (var i = 0; i<=8; i++){
//     setTimeout(() => {
//         console.log(i)
//     }, 5000);
// }
// console.log('hello')



