// react js
function NavBar() {
    return ( 
        <h1>Hello React</h1>
    )
}
ReactDOM.render(<NavBar/>, document.getElementById("root"))

// vanilla js
const h1 = document.createElement("h1")
h1.textContent = "This is certified imperative js"
h1.className = "header"
document.getElementById("root").append(h1)

const nav = (
    <div>
        <nav>
            <h1>My Website in react</h1>
            <ul>
                <li>Pricing</li>
                <li>About</li>
                <li>Contact</li>
            </ul>
        </nav>
    </div>
)

ReactDOM.render(nav, document.getElementById("test1"))