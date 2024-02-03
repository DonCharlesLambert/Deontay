import { useState, useEffect } from 'react';
import logo from '../images/logonn-transparent.png';
import logoText from '../images/texthd-transparent.png';
import './header.css'

function Header({searchString, setSearchString}) {
  const [localString, setLocalString] = useState(searchString);
  useEffect(() => {
    const timeoutId = setTimeout(() => setSearchString(localString), 500);
    return () => clearTimeout(timeoutId);
  }, [localString, setSearchString])

  return (
    <div>
      <header className="deontay-header">
        <div className="parted-logo">
            <img id={"logoImg"} src={logo} alt="logo" />
            <img id={"logoText"} src={logoText} alt="Deontay, expert Advisor" />
        </div>
        <input
            key={"dontChange"}
            type="text"
            placeholder={"Search for Strategies"}
            value={localString}
            onChange={(input) => setLocalString(input.target.value)}
         />
      </header>
    </div>
  );
}

export default Header;
