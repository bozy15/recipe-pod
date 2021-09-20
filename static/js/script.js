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
});
