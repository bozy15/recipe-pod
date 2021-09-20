// All JS contained in this file will run once the page has fully loaded
$(document).ready(function () {
  // ---- MATERIALIZE.JS ---- //
  // initialize the Sidebar
  $(".sidenav").sidenav({ edge: "right" });

  // initialize the collapsible
  $(".collapsible").collapsible();

  // initialize the select
  $("select").formSelect();

  // initialize the modal
  $(".modal").modal();

  // ---- CUSTOM JS ---- //

  // ADD RECIPE FORM JS
  // Add another input field for the user to add a new ingredient
  $("#new_ingredient").click(function (e) {
    // Prevents the page scroll to top
    e.preventDefault();
    $("#ingredient_list").append(
      `<div class="input-field col s12">
          <i class="fas fa-list prefix"></i>
          <input id="ingredients" type="text" name="ingredients" minlength="3" class="validate" required>
          <label class="add-recipe" for="ingredients">Ingredient</label>
          <a href="#" id="remove_ingredient" class="text-shadow wave-effect waves-light btn red right">Delete <i class="fas fa-trash"></i></a>
      </div>`
    );
  });

  // initialize the delete ingredient button
  $("#ingredient_list").on("click", "#remove_ingredient", function (e) {
    // Prevents the page scroll to top
    e.preventDefault();
    $(this).parent().remove();
  });

  // Add another input field for the user to add a new step
  $("#new_step").click(function (e) {
    // Prevents the page scroll to top
    e.preventDefault();
    $("#method_list").append(
      `<div class="input-field col s12">
          <i class="fas fa-list-ol prefix"></i>
          <textarea name="method" id="method" rows="2" class="materialize-textarea validate" minlength="3"
                    maxlength="300" required></textarea>
          <label class="add-recipe" for="method">Method</label>
          <a href="#" id="remove_method" class="text-shadow wave-effect waves-light btn red right">Delete <i class="fas fa-trash"></i></a>
      </div>`
    );
  });

  // Initialize the delete method button
  $("#method_list").on("click", "#remove_method", function (e) {
    // Prevents the page scroll to top
    e.preventDefault();
    $(this).parent().remove();
  });
  // END OF ADD RECIPE FORM JS

  //  FLASH MESSAGES
  // Fades out the flash message after 3 seconds
  $("#flashes").delay(3000).fadeOut(200);

  // Dont let user sign in if passwords don't match
  $(function () {
    $(".login-btn").click(function () {
      let password = $("#password").val();
      let confirmPassword = $("#confirm_password").val();
      if (password !== confirmPassword) {
        // Show error message
        $("#error_message").html("Username and or Password are incorrect");
        $("#error_message").fadeIn(200).delay(3000).fadeOut(200);
        // Clear username and password fields
        $("#username").val("");
        $("#password").val("");
        $("#confirm_password").val("");

        return false;
      }
      return true;
    });
  });


// This code was take from the CI task-manager mini project
 // Initialize the select
 $("select").formSelect();

 // Validates the Options dropdown in add_task.html
 /*
 * Two Varibles are created to match materialize's validation
 * If any select element has the the required attribute,
 * then we display them on the DOM but make them hidden with CSS
 * Using parent and child selectors, we check if any focused input,
 * either has or doesn't have ".disabled" class and then assign it the right variable 
 * 
 */
 validateMaterializeSelect();
 function validateMaterializeSelect() {
   let classValid = {
     "border-bottom": "1px solid #4caf50",
     "box-shadow": "0 1px 0 0 #4caf50",
   };
   let classInvalid = {
     "border-bottom": "1px solid #f44336",
     "box-shadow": "0 1px 0 0 #f44336",
   };
   if ($("select.validate").prop("required")) {
     $("select.validate").css({
       display: "block",
       height: "0",
       padding: "0",
       width: "0",
       position: "absolute",
     });
   }
   $(".select-wrapper input.select-dropdown")
     .on("focusin", function () {
       $(this)
         .parent(".select-wrapper")
         .on("change", function () {
           if (
             $(this)
               .children("ul")
               .children("li.selected:not(.disabled)")
               .on("click", function () {})
           ) {
             $(this).children("input").css(classValid);
           }
         });
     })
     .on("click", function () {
       if (
         $(this)
           .parent(".select-wrapper")
           .children("ul")
           .children("li.selected:not(.disabled)")
           .css("background-color") === "rgba(0, 0, 0, 0.03)"
       ) {
         $(this).parent(".select-wrapper").children("input").css(classValid);
       } else {
         $(".select-wrapper input.select-dropdown").on(
           "focusout",
           function () {
             if (
               $(this)
                 .parent(".select-wrapper")
                 .children("select")
                 .prop("required")
             ) {
               if (
                 $(this).css("border-bottom") != "1px solid rgb(76, 175, 80)"
               ) {
                 $(this)
                   .parent(".select-wrapper")
                   .children("input")
                   .css(classInvalid);
               }
             }
           }
         );
       }
     });
 }
});
