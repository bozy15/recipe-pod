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
      '<div class="input-field col s8"><input id="ingredient" type="text" class="validate"><label for="ingredient">Ingredient</label></div>'
    );
  });
});
