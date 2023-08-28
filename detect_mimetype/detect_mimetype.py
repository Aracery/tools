import mimetypes
import magic

def get_mime_type(filename):
    """Get the MIME type of a file.

    Args:
        filename (str): The file name.

    Returns:
        str: The MIME type.
    """
    mime_type, encoding = mimetypes.guess_type(filename)
    if mime_type is None:
        with open(filename, "rb") as f:
            mime_type = magic.from_buffer(f.read(4))

    print(f"from buffer: {magic.from_buffer(open(filename, 'rb').read(2048))}")
    print(f"from buffer: {magic.from_buffer(open(filename, 'rb').read(2048), mime=True)}")
    print(f"from_file: {magic.from_file(filename, mime=True)}")
    
    return mime_type



filename = '/home/sebastien/Desktop/SumTube/SumTube_0.1/GoogleImagen.wav'

# The file extension is incorrect.
mime_type = get_mime_type(filename)

print(mime_type)
