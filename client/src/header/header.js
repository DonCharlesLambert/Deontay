import logo from '../images/logonn-transparent.png';
import logoText from '../images/texthd-transparent.png';
import './header.css'

function Header() {
  return (
    <div>
      <header className="deontay-header">
        <div className="parted-logo">
            <img id={"logoImg"} src={logo} alt="logo" />
            <img id={"logoText"} src={logoText} alt="Deontay, expert Advisor" />
        </div>
        <input
            type="text"
            placeHolder={"Search for Strategies"}
            onChange={null}
         />
      </header>
    </div>
  );
}

export default Header;
