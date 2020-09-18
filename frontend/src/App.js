import React, {useState, useEffect} from 'react';

const App = () =>{
   const [products, setProducts] = useState([]);
   const [loading, setLoading] = useState(false)

   useEffect(()=>{
      fetch('/api/products')
      .then(response=>response.json())
      .then(response=>{
        setProducts(response)
        setLoading(true)
      })
      .catch(e=>console.log(e));
   },[]);

   return(
       <div>
       <h1> Hello World </h1>
       {!loading && (<h1>loading ... </h1>)}
        {loading && (
          <ul>
             {products.map(product=>(
                 <li key={product.id}>
                   <div>
                      <h3> {product.title} with {product.price} $ </h3>
                      <img src={product.image} alt={product.title} />
                   </div>
                 </li>
             )) }
          </ul>
        )}
      </div>
   );
}
export default App;