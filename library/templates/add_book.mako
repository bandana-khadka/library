<!DOCTYPE html>
<html lang="{{ '${request.locale_name}' }}">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="pyramid web application">
    <meta name="author" content="Pylons Project">
    <link rel="shortcut icon" href="${request.static_url('library:static/pyramid-16x16.png')}">

    <title>Add new book</title>

  </head>

#Form to add a new book in the library database
<body>
 <h3>Movie</h3>
 <form name="add_book" action="/books" method="POST">
    <table border="1" width="100%">
        <tr>
            <td>Name</td><td><input type="text" name="name" value=""/></td>
        </tr>
        <tr>
            <td>Author</td><td><input type="text" name="author" value="" /></td>
        </tr>
        <tr>
            <td>Description</td><td><input type="text" name="description" value=""/></td>
        </tr>
        <tr>
            <td>Date Published</td><td><input type="date" name="publication_date" value="" /></td>
        </tr>
        <tr>
            <td>Edition</td><td width="100%"><input type="text" name="edition" value="" /></td>
        </tr>
        <tr>
            <td>Address Published</td><td><input type="date" name="publication_address" value="" /></td>
        </tr>
    </table>
    <input type="submit" value="Update" />
 </form>
</body>
</html>