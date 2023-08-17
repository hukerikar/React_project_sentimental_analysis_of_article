import React from "react";


function Navbar()
{
    return(

            <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <div class="container-fluid">
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
                </button>
                <a class="navbar-brand" href="#">Srujan Hukerikar</a>
                <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="#">Home</a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link" href="https://www.youtube.com/watch?v=wa0IVAIqbo0&list=PLu0W_9lII9agx66oZnT6IyhcMIbUMNMdt&index=5">Link</a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link " href="#">Link 2</a>
                    </li>
                </ul>
                <form class="d-flex">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search"></input>
                    <button class="btn btn-outline-success" type="submit">Search</button>
                </form>
                </div>
            </div>
            </nav>
        
    );


}
export default Navbar;