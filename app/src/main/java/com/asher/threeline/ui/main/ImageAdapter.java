package com.asher.threeline.ui.main;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import com.asher.threeline.R;
import com.asher.threeline.db.IType;
import com.asher.threeline.db.bean.DbContent;

import java.util.List;

public class ImageAdapter extends BaseAdapter {

    private LayoutInflater mInflater;
    private List<DbContent> mDbContentList;

    public ImageAdapter(Context context, List<DbContent> dbContents) {
        mInflater = (LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
        mDbContentList = dbContents;
    }

    @Override
    public int getCount() {
        return null == mDbContentList ? 0 : mDbContentList.size();
    }

    @Override
    public Object getItem(int position) {
        return position;
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public int getItemViewType(int position) {
        if (null == mDbContentList || mDbContentList.isEmpty()) {
            return super.getItemViewType(position);
        }
        return mDbContentList.get(position).getType() == null ? IType.TYPE_INVALID :
                mDbContentList.get(position).getType();
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        DbContent dbContent = mDbContentList.get(position);
        int currentType = getItemViewType(position);
        switch (currentType) {
            case IType.TYPE_ARTICLE:
                recycleArticleViewHolder(dbContent, convertView, parent);
                break;
            case IType.TYPE_SENTENCE:
                recycleSentenceViewHolder(dbContent, convertView, parent);
                break;
            case IType.TYPE_MUSIC:
                recycleMusicViewHolder(dbContent, convertView, parent);
                break;
            case IType.TYPE_IMAGE:
                recycleImageViewHolder(dbContent, convertView, parent);
                break;
            default:
                break;
        }
        return convertView;
    }

    /**
     * recycler view holder
     *
     * @param dbContent
     * @param convertView
     * @param parent
     */
    private void recycleArticleViewHolder(DbContent dbContent, View convertView,
                                          ViewGroup parent) {
        ArticleViewHolder articleViewHolder = null;
        // 第一次没有加载convertView
        if (convertView == null) {
            convertView = mInflater.inflate(R.layout.layout_article_item, parent, false);
            articleViewHolder = new ArticleViewHolder();
            convertView.setTag(articleViewHolder);
        } else {
            articleViewHolder = (ArticleViewHolder) convertView.getTag();
        }
        setArticleData(dbContent, articleViewHolder);
    }

    private void recycleSentenceViewHolder(DbContent dbContent, View convertView,
                                           ViewGroup parent) {
        SentenceViewHolder sentenceViewHolder = null;
        if (convertView == null) {
            convertView = mInflater.inflate(R.layout.layout_sentence_item, parent, false);
            sentenceViewHolder = new SentenceViewHolder();
            convertView.setTag(sentenceViewHolder);
        } else {
            sentenceViewHolder = (SentenceViewHolder) convertView.getTag();
        }
        setSentenceData(dbContent, sentenceViewHolder);
    }

    private void recycleMusicViewHolder(DbContent dbContent, View convertView,
                                        ViewGroup parent) {
        MusicViewHolder musicViewHolder = null;
        if (convertView == null) {
            convertView = mInflater.inflate(R.layout.layout_music_item, parent, false);
            musicViewHolder = new MusicViewHolder();
            convertView.setTag(musicViewHolder);
        } else {
            musicViewHolder = (MusicViewHolder) convertView.getTag();
        }
        setMusicData(dbContent, musicViewHolder);
    }

    private void recycleImageViewHolder(DbContent dbContent, View convertView,
                                        ViewGroup parent) {
        ImageViewHolder imageViewHolder = null;
        if (convertView == null) {
            convertView = mInflater.inflate(R.layout.layout_image_item, parent, false);
            imageViewHolder = new ImageViewHolder();
            convertView.setTag(imageViewHolder);
        } else {
            imageViewHolder = (ImageViewHolder) convertView.getTag();
        }
        setImageData(dbContent, imageViewHolder);
    }

    /**
     * set article data
     *
     * @param article    data
     * @param viewHolder viewHolder
     */
    private void setArticleData(DbContent article, ArticleViewHolder viewHolder) {
        viewHolder.articleAuthor.setText(article.getAuthor());
        viewHolder.articleTitle.setText(article.getTitle());
    }

    private void setSentenceData(DbContent sentence, SentenceViewHolder viewHolder) {
        viewHolder.sentenceAuthor.setText(sentence.getAuthor());
        viewHolder.sentenceTitle.setText(sentence.getTitle());
    }

    private void setMusicData(DbContent music, MusicViewHolder viewHolder) {
        viewHolder.musicAuthor.setText(music.getAuthor());
        viewHolder.musicTitle.setText(music.getTitle());
//        viewHolder.musicCover.setImageResource(music.getImagePath());
    }

    private void setImageData(DbContent image, ImageViewHolder viewHolder) {
//        viewHolder.coverImg.setImageBitmap();
    }

    private class ArticleViewHolder {
        private TextView articleTitle;
        private TextView articleAuthor;
    }

    private class SentenceViewHolder {
        private TextView sentenceTitle;
        private TextView sentenceAuthor;
    }

    private class MusicViewHolder {
        private ImageView musicCover;
        private TextView musicTitle;
        private TextView musicAuthor;
    }

    private class ImageViewHolder {
        private ImageView coverImg;
    }
}
