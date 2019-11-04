import $ from "jquery";

$( function() {
    $("ButtonA").click(()=>{
        console.log("this button worked");
        // $.ajax(
        //     {
        //         url: "{% url  %}",
        //         success: (data)=>{
        //             //success function for what happens when the ajax request works
        //             for (let i;i<data.meals.length;i++) //for each meal item in the response
        //             {
        //                 $("#meallist").append("<li>" + data.meals[0]+ "</li>")
        //             }
        //         }

        //     }

        // )
    })

})