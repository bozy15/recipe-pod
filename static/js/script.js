// All JS contained in this file will run once the page has fully loaded
$(document).ready(function () {
  // initialize the Sidebar
  $(".sidenav").sidenav({ edge: "right" });

  // initialize the collapsible
  $(".collapsible").collapsible();

  // initialize the select
  $("select").formSelect();

  // Add another input field for the user to add a new ingredient
  $("#new_ingredient").click(function () {
    $("#ingredient_list").append(
      `<div class="input-field col s12">
          <i class="fas fa-list prefix"></i>
          <input id="ingredients" type="text" name="ingredients" minlength="3" class="validate" required>
          <label for="ingredients">Ingredient</label>
      </div>`
    );
  });

  // Add another input field for the user to add a new step
  $("#new_step").click(function () {
    $("#method_list").append(
      `<div class="input-field col s12">
          <i class="fas fa-list-ol prefix"></i>
          <textarea name="method" id="method" rows="2" class="materialize-textarea validate" minlength="3"
                    maxlength="300" required></textarea>
          <label for="method">Method</label>
      </div>`
    );
  });
});
