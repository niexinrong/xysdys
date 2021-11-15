
function changeImage()
{
    element=document.getElementById('myimage')
    if (element.src.match("bulbon"))
    {
        element.src="/static/images/pic_bulboff.gif";
    }
    else
    {
        element.src="/static/images/pic_bulbon.gif";
    }
}
