import { useEffect, useState } from "react";
import './slide-in.css'

function SlideIn({children}) {
    const [styles, setStyles] = useState({});
    useEffect(() => {
        setStyles({opacity: 1, marginRight: "0px"})
    }, [])
    return (
        <div className="slide-in" style={styles}>
            {children}
        </div>
    );
}

export default SlideIn;
