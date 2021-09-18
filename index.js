const express=require("express");
const app=express();
const port=3000;
app.use(require("body-parser").urlencoded({extended:false}));
app.use(express.json())
app.post("/",(req,res)=>{
  const name=req.body.name;
  const age=req.body.age;
  res.send("Dear "+name+", now I am well aware that your age is "+age+".....");
});


app.listen(port,()=>{
  console.log("App is listening....");
});
