import { useEffect, useState } from "react";
import "../styles/global.css";

export default function Home() {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        fetchPosts().then(data => setPosts(data));
    }, []);

    return (
        <div className="container">
            <h1>Launch Tracker</h1>
            {posts.map((post, index) => (
                <PostCard key={index} post={post} />
            ))}
        </div>
    );
}
