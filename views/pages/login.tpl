% include('layouts/header.tpl', title='Home Page')

<div class="row d-flex justify-content-center mt-5">
    <div class="col-lg-6">
        <h2 class="text-center">Login Form</h2>
        <form class="form-control p-5" method="POST" action="/login">
            <div class="form-group mb-2 p-1">
                <input type="text" class="form-control" name="email" placeholder="eg:email@example.com" />
            </div>
            <div class="form-group mb-2 p-1">
                <input type="password" class="form-control" name="password" placeholder="*********" />
            </div>
            <div class="form-group mb-2 p-1">
                <button type="submit" class="btn btn-outline-success">Login</button>
            </div>
        </form>
    </div>
</div>
% include('layouts/footer.tpl')